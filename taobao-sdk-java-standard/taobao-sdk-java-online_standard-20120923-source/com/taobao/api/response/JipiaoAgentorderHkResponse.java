package com.taobao.api.response;

import com.taobao.api.internal.mapping.ApiField;

import com.taobao.api.TaobaoResponse;

/**
 * TOP API: taobao.jipiao.agentorder.hk response.
 * 
 * @author auto create
 * @since 1.0, null
 */
public class JipiaoAgentorderHkResponse extends TaobaoResponse {

	private static final long serialVersionUID = 4812481719993576966L;

	/** 
	 * hk(占座)是否成功
	 */
	@ApiField("is_success")
	private Boolean isSuccess;

	public void setIsSuccess(Boolean isSuccess) {
		this.isSuccess = isSuccess;
	}
	public Boolean getIsSuccess( ) {
		return this.isSuccess;
	}

}
